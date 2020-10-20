#!/usr/bin/env python3

"""
Collect all GitHub repositories from active/rolling ROS distributions.

For each repo a mapping from branches to ROS distros is stored.

This generates the file `data/repos.yaml`.
"""

import os
import sys

from rosdistro import get_cached_distribution
from rosdistro import get_index
from rosdistro import get_index_url

import yaml

repos = {}

index = get_index(get_index_url())
for name, d in index.distributions.items():
    if d['distribution_status'] not in ('active', 'rolling'):
        continue
    d = get_cached_distribution(index, name)
    for r in d.repositories.values():
        if r.source_repository is None:
            continue
        sr = r.source_repository
        if sr.type != 'git':
            continue
        prefix = 'https://github.com/'
        suffix = '.git'
        if not sr.url.startswith(prefix) or not sr.url.endswith(suffix):
            continue
        url = sr.url[len(prefix):-len(suffix)]

        print('*', end='')
        sys.stdout.flush()

        versions = repos.setdefault(url, {})
        distros = versions.setdefault(sr.version, [])
        distros.append(name)

os.makedirs('data', exist_ok=True)
with open('data/repos.yaml', 'w') as h:
    yaml.dump(repos, h)

print()
print(
    len(repos), 'repos with',
    sum(len(versions) for versions in repos.values()), 'branches')
