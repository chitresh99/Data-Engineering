# Stage 1: Build stage
FROM gcc:11 as builder

# RUN: Install cmake
RUN apt-get update && apt-get install -y cmake

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy CMake files first
COPY CMakeLists.txt .

# COPY: Copy source code
COPY main.cpp .

# RUN: Build application
RUN mkdir build && cd build && \
    cmake .. && \
    make

# Stage 2: Production stage
FROM debian:bookworm-slim

# RUN: Install runtime dependencies and create user
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash app

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy binary from builder
COPY --from=builder /app/build/webapp .

# USER: Switch to non-root user
USER app

# EXPOSE: Document port
EXPOSE 8080

# ENV: Set environment variable
ENV ENVIRONMENT=production

# CMD: Run application
CMD ["./webapp"]