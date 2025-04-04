FROM node:18.14.2

# Create a non-root user
RUN useradd -m -s /bin/bash nodeuser
USER nodeuser

# Set Node.js memory limit
ENV NODE_OPTIONS="--max-old-space-size=8192"

# Install cspell globally (security fix: use --ignore-scripts)
RUN npm install -g cspell@5.19.0 --ignore-scripts

# Set working directory
WORKDIR /app

# Copy necessary files
COPY cspell.json ./ 
COPY custom-words.txt ./

# Define entry point
ENTRYPOINT ["cspell"]
