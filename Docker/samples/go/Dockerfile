# Stage 1: Build stage
FROM golang:1.21-alpine AS builder

# RUN: Install git and ca-certificates
RUN apk add --no-cache git ca-certificates

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy go mod files first (dependency caching)
COPY go.mod go.sum ./

# RUN: Download dependencies
RUN go mod download

# COPY: Copy source code
COPY . .

# RUN: Build the application
# CGO_ENABLED=0: Disable CGO for static binary
# GOOS=linux: Target Linux OS
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Stage 2: Production stage
FROM alpine:latest

# RUN: Install ca-certificates and create non-root user
RUN apk --no-cache add ca-certificates \
    && adduser -D -s /bin/sh app

# WORKDIR: Set working directory
WORKDIR /root/

# COPY: Copy binary from builder stage
COPY --from=builder /app/main .

# USER: Switch to non-root user
USER app

# EXPOSE: Document port
EXPOSE 8080

# ENV: Set environment variable
ENV ENVIRONMENT=production

# HEALTHCHECK: Add health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

# CMD: Run the application
CMD ["./main"]