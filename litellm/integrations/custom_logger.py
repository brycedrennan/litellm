#### What this does ####
#    On success, logs events to Promptlayer
import dotenv, os
import requests
import requests
import inspect
import asyncio

dotenv.load_dotenv()  # Loading env variables using dotenv
import traceback


class CustomLogger:
    # Class variables or attributes
    def __init__(self):
        pass

    def log_pre_api_call(self, model, messages, kwargs): 
        pass

    def log_post_api_call(self, kwargs, response_obj, start_time, end_time): 
        pass
    
    def log_stream_event(self, kwargs, response_obj, start_time, end_time):
        pass

    def log_success_event(self, kwargs, response_obj, start_time, end_time): 
        pass

    def log_failure_event(self, kwargs, response_obj, start_time, end_time): 
        pass


    #### DEPRECATED ####

    def log_input_event(self, model, messages, kwargs, print_verbose, callback_func):
        try: 
            kwargs["model"] = model
            kwargs["messages"] = messages
            kwargs["log_event_type"] = "pre_api_call"
            callback_func(
                kwargs,
            )
            print_verbose(
                f"Custom Logger - model call details: {kwargs}"
            )
        except: 
            traceback.print_exc()
            print_verbose(f"Custom Logger Error - {traceback.format_exc()}")

    def log_event(self, kwargs, response_obj, start_time, end_time, print_verbose, callback_func):
        # Method definition
        try:
            kwargs["log_event_type"] = "post_api_call"
            if inspect.iscoroutinefunction(callback_func):
                # If it's async, use asyncio to run it

                loop = asyncio.get_event_loop()
                if loop.is_closed():
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                loop.run_until_complete(callback_func(kwargs, response_obj, start_time, end_time))
            else:
                # If it's not async, run it synchronously
                callback_func(
                    kwargs,  # kwargs to func
                    response_obj,
                    start_time,
                    end_time,
                )
            print_verbose(
                f"Custom Logger - final response object: {response_obj}"
            )
        except Exception as e:
            raise e
            # traceback.print_exc()
            print_verbose(f"Custom Logger Error - {traceback.format_exc()}")
            pass
