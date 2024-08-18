#!/usr/bin/env python
import sys
from crew.crew import MarketResearchCrew
from flask import Flask, request, Response, stream_with_context, send_file
from threading import Thread
import queue
import os
from flask_cors import CORS

import agentops

agentops.init()

app = Flask(__name__)
CORS(app)

def run_crew(inputs, output_queue):
    """
    Run the market research crew and put output in the queue.
    """
    def custom_print(*args, **kwargs):
        output = " ".join(map(str, args))
        output_queue.put(output + "\n")

    import builtins
    builtins.print = custom_print

    MarketResearchCrew().crew().kickoff(inputs=inputs)
    output_queue.put(None)  # Signal that the process is complete

@app.route('/run_crew', methods=['POST'])
def run_crew_service():
    inputs = request.json
    output_queue = queue.Queue()

    thread = Thread(target=run_crew, args=(inputs, output_queue))
    thread.start()

    def generate():
        while True:
            output = output_queue.get()
            if output is None:
                break
            yield output

    return Response(stream_with_context(generate()), content_type='text/plain')

@app.route('/get_recommendation', methods=['GET'])
def get_recommendation():
    if os.path.exists('report.md'):
        with open('report.md', 'r') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/markdown'}
    else:
        return "Recommendation not available", 404

def run():
    """
    Run the market research crew.
    """
    inputs = {
        'industry': input("Enter the industry: "),
        'use_case': input("Enter the use case: "),
        'other_requirements': input("Enter any other requirements (optional): ")
    }
    MarketResearchCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'industry': input("Enter the industry: "),
        'use_case': input("Enter the use case: "),
        'other_requirements': input("Enter any other requirements (optional): ")
    }
    try:
        MarketResearchCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MarketResearchCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        app.run(host='0.0.0.0', port=5000)
    else:
        run()