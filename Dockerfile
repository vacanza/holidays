FROM node:18.14.2


# Set Node.js memory limit
ENV NODE_OPTIONS="--max-old-space-size=8192"

# Install cspell globally
RUN npm install -g cspell@5.19.0


# Set working directory
WORKDIR /app

# Copy necessary files
COPY cspell.json ./ 
COPY custom-words.txt ./

# Define entry point
ENTRYPOINT ["cspell"]
