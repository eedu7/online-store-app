interface ApiErrorDetail {
  message: string;
  error_code?: string;
  details?: Record<string, unknown>;
}

export class ApiError extends Error {
  status: number;
  error_code?: string;
  details?: Record<string, unknown>;

  constructor(status: number, detail: ApiErrorDetail) {
    super(detail.message);
    this.status = status;
    this.error_code = detail.error_code;
    this.details = detail.details;
  }
}
