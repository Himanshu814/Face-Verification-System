# Face-Verification-System

## Overview

The Face Verification System is an advanced application designed to facilitate secure and efficient identity verification using facial recognition technology. This system is tailored for applications such as secure voting processes, access control, and identity management. Built with Python, it leverages OpenCV, Tkinter, and MySQL to provide a robust and interactive user experience.

## Features
### 1. Face Recognition and Verification:

- Identify and verify users based on their facial features.
- Display verification results in real-time.

### 2. Voter Management:

- Add, update, and delete voter details.
- Manage voter-specific attributes, including images and personal details.

### 3. Dataset Training:

- Train the system with labeled datasets using the LBPH (Local Binary Patterns Histograms) algorithm.
- Generate and save training models for future use.
### 4. Real-Time Interaction:

- Capture live data using webcams for image acquisition and verification.
- Real-time validation with high accuracy thresholds.

### 5. Data Export/Import:

- Export verified data to CSV.
- Import existing voter details from CSV.



## Technologies Used

**1] Programming Language**: Python

**2] Libraries:**
- OpenCV (Computer Vision)
- Tkinter (GUI)
- PIL (Image Processing)
- NumPy
- MySQL Connector

**3] Database:** MySQL

## Prerequisites

**Python 3.7 or later:**

- Required Python libraries:

pip install opencv-python-headless pillow mysql-connector-python numpy

**MySQL Server**:

- Ensure MySQL is installed and running.
- Configure your database with the necessary tables (refer to the database scripts in the project).

## Project Structure

- **main.py:** Entry point of the application with GUI integration.

- **voter.py:** Module for managing voter details.

- **train.py:** Handles dataset training and model generation.

- **recognition.py**: Core facial recognition and verification logic.

- **verification.py:** Implements CSV import/export and verified user management.

- **data:** Directory to store captured and trained images.

## How It Works

1] **Add Voter Details:**
Use the GUI to input personal details and capture image samples.

2] **Train Dataset:**
Train the model using the stored voter images.

3] **Verify Voters:**
Use the facial recognition feature to match users against the trained dataset.

4] **Export Verified Data:**
Save verified records for auditing or reporting purposes.
