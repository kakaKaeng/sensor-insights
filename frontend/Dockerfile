FROM node:22.11.0 AS builder

WORKDIR /app

ARG VITE_API_HOST
ARG VITE_API_KEY
ENV VITE_API_HOST=$VITE_API_HOST
ENV VITE_API_KEY=$VITE_API_KEY

COPY . .

RUN npm install && npm run build


FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]