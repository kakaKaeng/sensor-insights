import { config } from '@/config.ts';
import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios';

export class BaseApiService {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: config.API_HOST,
      headers: { 'Content-Type': 'application/json', 'X-Api-Key': config.API_KEY },
    });
  }

  get<TResponse = unknown>(
    url: string,
    config: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<TResponse>> {
    return this.client.get(url, config);
  }

  post<TRequest = unknown, TResponse = unknown>(
    url: string,
    data: TRequest,
    config: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<TResponse>> {
    return this.client.post(url, data, config);
  }
}
