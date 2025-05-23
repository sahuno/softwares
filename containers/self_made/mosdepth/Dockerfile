FROM debian:buster-slim

LABEL maintainer="sahuno"

ARG MOSDEPTH_VERSION=0.3.11
ENV MOSDEPTH_VERSION=${MOSDEPTH_VERSION}

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         ca-certificates \
         curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fSL \
      "https://github.com/brentp/mosdepth/releases/download/v${MOSDEPTH_VERSION}/mosdepth" \
      -o /usr/local/bin/mosdepth \
    && chmod +x /usr/local/bin/mosdepth

ENTRYPOINT ["mosdepth"]
CMD ["--help"]