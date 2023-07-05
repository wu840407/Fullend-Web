# Use the official Node.js 14 base image
FROM node:18 AS builder

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json files
COPY package*.json ./

# Install Angular CLI and project dependencies
RUN npm install -g npm@latest
RUN npm install -g @angular/cli@latest
RUN npm install

# Copy the entire project directory into the container
COPY . .

# Build the Angular application
RUN ng build

# Use the official Nginx base image
FROM nginx:latest

# Copy the built Angular app to the Nginx document root directory
COPY --from=builder /usr/src/app/dist/frontend /usr/share/nginx/html

# Expose port 8443
EXPOSE 8443

# Start Nginx when the container is run
CMD ["nginx", "-g", "daemon off;"]
