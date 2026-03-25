import { ApiError } from "./error";

export function getErrorMessage(error: unknown): {
  message: string;
  severity: "error" | "warning";
} {
  if (!(error instanceof ApiError)) {
    return {
      message: "Something went wrong. Please try again.",
      severity: "error",
    };
  }

  switch (error.error_code) {
    case "PERMISSION_DENIED":
      return {
        message: `You don't have permission to do this.`,
        severity: "error",
      };
    case "DUPLICATE_VALUE":
      return {
        message: "This entry already exists.",
        severity: "warning",
      };
  }

  switch (error.status) {
    case 400:
      return {
        message: "Invalid request.",
        severity: "error",
      };
    default:
      return {
        message: error.message || "An unexpected error occurred.",
        severity: "error",
      };
  }
}
