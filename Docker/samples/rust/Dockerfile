# Stage 1: Build stage
FROM rust:1.70 as builder

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy Cargo files first (dependency caching)
COPY Cargo.toml Cargo.lock ./

# RUN: Create dummy main.rs to build dependencies
RUN mkdir src && echo "fn main() {}" > src/main.rs

# RUN: Build dependencies
RUN cargo build --release

# RUN: Remove dummy main.rs
RUN rm src/main.rs

# COPY: Copy actual source code
COPY src ./src

# RUN: Build application
RUN cargo build --release

# Stage 2: Production stage
FROM debian:bookworm-slim

# RUN: Install runtime dependencies and create user
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash app

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy binary from builder
COPY --from=builder /app/target/release/webapp .

# USER: Switch to non-root user
USER app

# EXPOSE: Document port
EXPOSE 3030

# ENV: Set environment variable
ENV ENVIRONMENT=production

# CMD: Run application
CMD ["./webapp"]