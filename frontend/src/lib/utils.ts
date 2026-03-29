import {type ClassValue, clsx} from "clsx";
import {differenceInDays, format, formatDistanceToNow, parseISO,} from "date-fns";
import {twMerge} from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatDate(isoDate: string): string {
  const date = parseISO(isoDate);

  const daysDiff = differenceInDays(new Date(), date);

  // If difference is more than 7 days, show full date, else relative
  if (daysDiff > 7) {
    return format(date, "MMM d, yyyy");
  } else {
    return formatDistanceToNow(date, { addSuffix: true });
  }
}
