FROM node:20-alpine

# Set working directory for node modules installation
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install cspell and dictionaries locally using npm ci with security flags
RUN npm ci --ignore-scripts --no-audit --no-fund && npm cache clean --force

# Set working directory for the application
WORKDIR /holidays

# Copy cspell configuration and custom dictionary
COPY cspell.json cspell/cspell.json
COPY custom-dict.txt cspell/custom-dict.txt

# Use non-root user for security
USER node

# Set entrypoint to local cspell binary
ENTRYPOINT ["/app/node_modules/.bin/cspell"]
CMD ["--help"]
