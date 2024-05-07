FROM python:3.10-slim

#ENV PYTHONBUFFERED=1

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         build-essential \
#         cmake \
#         unzip \
#         libopenblas-dev \
#         liblapack-dev \
#         libjpeg-dev \
#         libpng-dev \
#         libtiff-dev \
#         libgtk-3-dev \
#     && rm -rf /var/lib/apt/lists/*

# Copy the CMake installer to the container
# COPY cmake-3.29.2-windows-x86_64.zip C:/cmake-3.29.2-windows-x86_64.zip

# # Extract the contents of the ZIP file
# RUN unzip C:/cmake-3.29.2-windows-x86_64.zip -d C:/cmake

# # Add the CMake binary directory to the PATH
# ENV PATH="/cmake/bin:${PATH}"
WORKDIR /django

COPY dependencies.txt dependencies.txt

RUN pip3 install -r dependencies.txt

EXPOSE 8000

COPY . .

CMD python website.py runserver 0.0.0.0:8000