import * as z from "zod"
import { generateText, Output } from "ai";
import { google } from "@ai-sdk/google";

const x = z.object({
  foo: z.string()
})

export async function playEncounter() {
  const { output } = await generateText({
    model: google(""),
    prompt: "",
    output: Output.object({ schema: x }),
  })
}
