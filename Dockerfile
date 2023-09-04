FROM python:3.9-slim-buster

# Install OpenAI Whisper
RUN pip install openai-whisper

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Enable venv
ENV PATH="/build/venv/bin:$PATH"
# Install Jupyter lab
RUN pip3 install jupyter ipywidgets jupyterlab pandas numpy 
#copy utils 
COPY /utils /app/utils

#Copy data 
COPY /data_videos/data_videos_con_url.json /app

# Copy Jupyter notebook
COPY 7_whisper.ipynb /app/7_whisper.ipynb

# Set working directory
WORKDIR /app

# Expose port 8888 for Jupyter notebook
EXPOSE 8888



# Start the Jupyter Notebook server
CMD ["jupyter", "lab", "--ip=0.0.0.0","--no-browser", "--port=8888", "--allow-root"]
