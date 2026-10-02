# --- Build stage ---
FROM python:3.12-alpine AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Runtime stage ---
FROM python:3.12-alpine
WORKDIR /app

# Security: run as non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --chown=appuser:appgroup --from=build /install/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --chown=appuser:appgroup . .
USER appuser

# Metadata for governance/tracking
LABEL maintainer="khaledalajam9@gmail.com" \
      org.opencontainers.image.source="https://github.com/khaledalajam/cloud-platform-demos" \
      org.opencontainers.image.description="Sample platform service"

EXPOSE 3000

# Observability: container-level health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["python", "server.py"]   
