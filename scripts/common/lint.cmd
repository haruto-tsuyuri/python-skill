set linux_path=%REMOTE_FILE_PATH:\=/%

docker run ^
       --init ^
       --rm ^
       -v %LOCAL_FILE_PATH%:/usr/app/%linux_path% ^
       py-study:3.10 ^
       /bin/sh -c "black %linux_path% && isort --profile black %linux_path%"