FROM python:3.12-alpine
WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --chown=appuser:appgroup . .
USER appuser

LABEL maintainer="khaledalajam9@gmail.com" \
      org.opencontainers.image.source="https://github.com/khaledalajam/cloud-platform-demos" \
      org.opencontainers.image.description="Sample platform service"

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["python", "server.py"]   
