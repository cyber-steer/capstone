# SD 카드 준비
```
diskpart
list disk
select disk 1 // SD카드에 해당되는 번호로
list partition // 해당 디스크가 SD카드인지 확인
clean
```

# img 파일 준비
[https://developer.nvidia.com/embedded/downloads](https://developer.nvidia.com/embedded/downloads)<br>
Jetson Nano Developer Kit SD Card Image 4.6.1 파일 다운로드

# OS 쓰기
[https://etcher.balena.io/](https://etcher.balena.io/)<br>
1. 이미지 선택
2. SD카드 선택
3. 이미지 쓰기

# 프로젝트 설정
```Bash
git clone -b nano https://github.com/cyber-steer/capstone.git
cd capstone
sudo bash init.sh
python3 -m pip install .
reboot
```

# 프로젝트 실행
```Python
python3 capstone/main.py
```

# 쿨러 사용
[https://github.com/jugfk/jetson-fan-ctl](https://github.com/jugfk/jetson-fan-ctl)
```Bash
git clone https://github.com/jetsonworld/jetson-fan-ctl.git
cd jetson-fan-ctl
sudo sh install.sh
```
# 회로 구성
![회로구성](https://github.com/cyber-steer/capstone/blob/nano/img/doorlock.jpg)