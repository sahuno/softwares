#!/usr/bin/env bash
set -euo pipefail

IMAGE="sahuno/onttools:latest"

echo "Setting up multi-arch builder 'multiarch-builder'..."
if docker buildx inspect multiarch-builder >/dev/null 2>&1; then
  echo "Found existing builder 'multiarch-builder', switching to it"
  docker buildx use multiarch-builder
else
  echo "Creating new builder 'multiarch-builder'"
  docker buildx create --name multiarch-builder --use --bootstrap
fi

echo "Building and pushing image $IMAGE for linux/amd64 and linux/arm64..."
echo "Ensure you are logged in to Docker Hub (docker login)"
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag "$IMAGE" \
  --push \
  .