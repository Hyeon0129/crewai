import sys
from datetime import datetime
from report_automation.crew import ReportAutomation


def run():
    topic = sys.argv[1] if len(sys.argv) > 1 else input("Enter topic: ")
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    ReportAutomation().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
