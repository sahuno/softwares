# softwares

**Author**: Samuel Ahuno  
**Purpose**: Centralised Docker/Singularity container definitions and custom packages for computational biology

---

## Repository structure

```
softwares/
├── containers/
│   ├── self_made/          # Dockerfiles built and pushed to Docker Hub via CI
│   │   ├── dorado/         # ONT Dorado basecaller
│   │   ├── dockerR/        # R analysis environment
│   │   ├── ML_numpyro/     # NumPyro ML environment
│   │   ├── ML_pyro/        # Pyro ML environment
│   │   ├── ONT_tools/      # ONT long-read analysis tools
│   │   ├── mosdepth/       # Coverage analysis
│   │   └── pfamtools/      # Pfam annotation tools
│   └── others/             # Third-party / reference definition files
└── packages/
    ├── python/             # methylHelper
    └── R/                  # methylONT (R package)
```

---

## Docker CI — automated builds

All Dockerfiles under `containers/self_made/` are built and pushed to Docker Hub (`sahuno/<tool>:<version>`) automatically via GitHub Actions.

**Tag format**: `{tool}-v{version}`  
**Images pushed to**: `sahuno/{tool}:{version}` and `sahuno/{tool}:latest`

### Add a new tool

```bash
# 1. Create a directory matching the intended Docker Hub image name
mkdir containers/self_made/<tool>

# 2. Add a Dockerfile
cp /path/to/Dockerfile containers/self_made/<tool>/Dockerfile

# 3. Commit and push
git add containers/self_made/<tool>/
git commit -m "Add <tool> container"
git push

# 4. Tag to trigger the build
git tag <tool>-v<version>
git push origin <tool>-v<version>
# e.g. git tag modkit-v0.4.0 && git push origin modkit-v0.4.0
```

Image will be available as `sahuno/<tool>:<version>` and `sahuno/<tool>:latest`.

### Rebuild / update an existing tool

```bash
# Edit the Dockerfile
vim containers/self_made/<tool>/Dockerfile

git add containers/self_made/<tool>/Dockerfile
git commit -m "Update <tool> to v<new_version>"
git push

# Tag the new version to trigger rebuild
git tag <tool>-v<new_version>
git push origin <tool>-v<new_version>
# e.g. git tag dorado-v1.5.0 && git push origin dorado-v1.5.0
```

### Trigger a build manually (no tag needed)

```bash
gh workflow run docker-build.yml \
  --repo sahuno/softwares \
  -f tool=<tool> \
  -f version=<version>

# e.g.
gh workflow run docker-build.yml \
  --repo sahuno/softwares \
  -f tool=dorado \
  -f version=1.4.0
```

### Monitor a build

```bash
gh run list --repo sahuno/softwares --limit 5
gh run watch --repo sahuno/softwares
```

### Pull a built image on HPC (Apptainer)

```bash
apptainer pull docker://sahuno/<tool>:<version>
# e.g.
apptainer pull docker://sahuno/dorado:1.4.0
```

---

## Packages

| Package | Language | Description |
|---------|----------|-------------|
| methylHelper | Python | ONT methylation analysis utilities |
| methylONT | R | ONT methylation analysis (R package) |
