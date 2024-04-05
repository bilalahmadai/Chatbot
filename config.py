config={
    "openai_chat_model": 
        {
            "gpt-3.5-turbo-0125":{
                "DESCRIPTION":"""\
                    New Updated GPT 3.5 Turbo
                    The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens.
                """,
                "CONTEXT WINDOW":"16,385 tokens",
                "TRAINING DATA":"Up to Sep 2021"
            },

            "gpt-3.5-turbo":{
                "DESCRIPTION":"""\
                    Currently points to gpt-3.5-turbo-0125.
                """,
                "CONTEXT WINDOW":"16,385 tokens",
                "TRAINING DATA":"Up to Sep 2021"
            },
            "gpt-3.5-turbo-1106":{
                "DESCRIPTION":"""\
                    GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens.
                """,
                "CONTEXT WINDOW":"16,385 tokens",
                "TRAINING DATA":"Up to Sep 2021"
            },

        }
}

