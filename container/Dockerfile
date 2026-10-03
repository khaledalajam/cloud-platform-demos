name: Build & Push

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      packages: write
      contents: read
    env:
      SHA: ${{ github.sha }}
    steps:
      - uses: actions/checkout@v4

      - name: Build & Tag
        run: |
          TAG="${SHA:0:7}"
          docker build -t ghcr.io/${{ github.repository_owner }}/platform-container:$TAG ./container
          docker tag ghcr.io/${{ github.repository_owner }}/platform-container:$TAG \
                    ghcr.io/${{ github.repository_owner }}/platform-container:latest
          docker images | grep platform-container

      - name: Login to GHCR
        run: echo "${{ secrets.GHCR_PAT }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Push
        run: |
          TAG="${SHA:0:7}"
          docker push ghcr.io/${{ github.repository_owner }}/platform-container:$TAG
          docker push ghcr.io/${{ github.repository_owner }}/platform-container:latest   
