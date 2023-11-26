# Dockerfile
FROM python:3.10.9

# Install prerequisites
# RUN apt-get update && apt-get install -y \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg \
#     lsb-release

# Install Docker
# RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# RUN echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
# RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io

COPY collector2.py /app/collector2.py

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "collector2.py"]
# CMD ["sh", "-c", "service docker start && python collector2.py"]
