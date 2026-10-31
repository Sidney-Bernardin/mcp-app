export const domainErrorTypes = ["username_taken"] as const
type DomainErrorsType = typeof domainErrorTypes[number]

export type Result<T, E = Error> = [T, err: undefined] | [undefined, E]

export async function tryCatch<T, E = Error>(promise: Promise<T>): Promise<Result<T, E>> {
  try {
    return [await promise, undefined]
  } catch (err) {
    return [undefined, err as E]
  }
}

export class DomainError extends Error {
  constructor(public type: DomainErrorsType, msg: string) {
    super(msg)
    this.type = type
  }
}
