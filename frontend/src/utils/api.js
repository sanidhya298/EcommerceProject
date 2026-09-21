const configuredBaseUrl = import.meta.env.VITE_DJANGO_BASE_URL || "http://127.0.0.1:8000";

export const API_BASE_URL = configuredBaseUrl.replace(/\/+$/, "");

export const mediaUrl = (path) => {
  if (!path) return "";
  if (path.startsWith("http://") || path.startsWith("https://")) return path;
  return `${API_BASE_URL}/${path.replace(/^\/+/, "")}`;
};