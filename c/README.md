To compile:

    Setup cross compiling with:

    mkdir /home/alex/raspberry_pi_tools
    cd /home/alex/raspberry_pi_tools
    git clone git://github.com/raspberrypi/tools.git
    /home/alex/raspberry_pi_tools/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-gcc -v

    Then compile with:

    /home/alex/raspberry_pi_tools/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-gcc src/*.c /home/alex/github/alexcb/music-control/c/third_party/wiringPi/wiringPi/*.c -I/home/alex/github/alexcb/music-control/c/third_party/wiringPi/wiringPi/ -lpthread

