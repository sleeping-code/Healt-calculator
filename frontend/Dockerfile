# Dockerfile for the Frontend Application

# Use a lightweight Nginx image as the base
# Nginx is an excellent choice for serving static web content
FROM nginx:alpine

# Copy the static HTML, CSS, and JS files into the Nginx web root directory
# The default Nginx web root is /usr/share/nginx/html
COPY . /usr/share/nginx/html

# Expose port 80, which is the default HTTP port Nginx listens on
EXPOSE 80

# The default command for nginx:alpine starts Nginx, so no CMD is needed here.
# If you needed to run a custom command, you would specify it with CMD.
