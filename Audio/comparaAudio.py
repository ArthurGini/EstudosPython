# Codigo baseado em:
# https://medium.com/@shivama205/audio-signals-comparison-23e431ed2207
""" Estudo futuro:
https://towardsdatascience.com/a-data-scientists-approach-to-visual-audio-comparison-fa15a5d3dcef


"""


#comparaAudio.py
from correlation import correlate

import argparse

def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--source-file",help="source file")
    parser.add_argument("-o", "--source-file",help="source file")
    args = parser.parse_args()

    SOURCE_FILE = args.source_file if args.source_file else None
    TARGET_FILE = args.target_file if args.target_file else None
    if not SOURCE_FILE or not TARGET_FILE:
        raise Exception("Arquivo target não especificado.")
    return SOURCE_FILE, TARGET_FILE

if __name__ == "__main__":
    SOURCE_FILE, TARGET_FILE = initialize()
#    correlate(SOURCE_FILE, TARGET_FILE)