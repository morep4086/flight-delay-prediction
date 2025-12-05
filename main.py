#!/usr/bin/env python3
"""
Main entry point for the Flight Delay Prediction project
"""

import os
import sys
import argparse

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.train import train_models
from src.models.evaluate import evaluate
from src.models.predict import predict

def main():
    parser = argparse.ArgumentParser(description='Flight Delay Prediction System')
    parser.add_argument('action', choices=['train', 'evaluate', 'predict'], 
                       help='Action to perform')
    parser.add_argument('--input', help='Input CSV file for prediction')
    
    args = parser.parse_args()
    
    if args.action == 'train':
        print("Training models...")
        train_models()
        
    elif args.action == 'evaluate':
        print("Evaluating model...")
        evaluate()
        
    elif args.action == 'predict':
        if args.input:
            print(f"Making predictions on {args.input}...")
            predict(args.input)
        else:
            print("Making predictions on default dataset...")
            predict()

if __name__ == '__main__':
    main()