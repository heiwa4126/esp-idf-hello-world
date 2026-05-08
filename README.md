# esp-idf-hello-world

(2026-05) [esp\-idf/examples/get\-started/hello_world at master · espressif/esp\-idf · GitHub](https://github.com/espressif/esp-idf/tree/master/examples/get-started/hello_world)
をやってみた。

環境は

- ESP32-WROVER のカメラ付きのやつ([FNK0060](https://www.amazon.co.jp/dp/B0CJJHXD1W))
- Windows11 の WSL2(Ubuntu)上で開発
- IDF は 6.1
- [EIM (ESP-IDF Installation Manager)](https://docs.espressif.com/projects/idf-im-ui/en/latest/) なしでやってみたら、やっぱいろいろ辛いので、EIM 試す

手順はこんな感じ:

0. Windows 側で usbipd.exe(`winget install dorssel.usbipd-win`) と [CH340 ドライバ](https://www.wch-ic.com/search?q=CH340&t=downloads)(ESP32-WROVER だから)
1. [USB デバイスを接続する](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb#attach-a-usb-device) で WSL に接続
1. [ステップ1\. 前提条件のインストール](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-1-install-prerequisites)
1. [ステップ2\. ESP\-IDFを取得する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-2-get-esp-idf) - でかい。2.4G あった
1. [ステップ3．ツールをセットアップする](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-3-set-up-the-tools) - とりあえず毎回 `. $HOME/esp/esp-idf/export.sh` を実行することにする
1. [プロジェクトを開始する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#start-a-project) - パスは`~/esp/hello_world` でなくてもどこでも OK
1. [プロジェクトの設定](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#configure-your-project) - TUI のメニューは何もしないで `Q`
1. [プロジェクトを構築する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#build-the-project)
1. [デバイスにフラッシュする](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#flash-onto-the-device) - ここで PORT に `/dev/ttyUSB0`
1. [出力を監視する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#monitor-the-output) - ここでも PORT に `/dev/ttyUSB0`

毎回

```sh
. $HOME/esp/esp-idf/export.sh
code .
```

は面倒。あと IDF の VScode 拡張がいろいろうるさいのもやだ。EIM にするといいらしいのであとで試す。

## 出力例

`idf.py -p /dev/ttyUSB0 monitor` の出力例

```console
ets Jul 29 2019 12:21:46

rst:0xc (SW_CPU_RESET),boot:0x1b (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0040,len:6272
load:0x40078000,len:15848
load:0x40080400,len:3988
--- 0x40080400: _invalid_pc_placeholder at /home/heiwa/esp/esp-idf/components/xtensa/xtensa_vectors.S:2259
entry 0x40080644
--- 0x40080644: call_start_cpu0 at /home/heiwa/esp/esp-idf/components/bootloader/subproject/main/bootloader_start.c:27
I (27) boot: ESP-IDF v6.1-dev-4506-g88add2513f 2nd stage bootloader
I (27) boot: compile time May  7 2026 18:26:21
I (27) boot: Multicore bootloader
I (30) boot: chip revision: v3.1
I (33) boot.esp32: SPI Speed      : 40MHz
I (37) boot.esp32: SPI Mode       : DIO
I (40) boot.esp32: SPI Flash Size : 2MB
I (44) boot: Enabling RNG early entropy source...
I (48) boot: Partition Table:
I (51) boot: ## Label            Usage          Type ST Offset   Length
I (57) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (64) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (70) boot:  2 factory          factory app      00 00 00010000 00100000
I (77) boot: End of partition table
I (80) esp_image: segment 0: paddr=00010020 vaddr=3f400020 size=06dach ( 28076) map
I (98) esp_image: segment 1: paddr=00016dd4 vaddr=3ffb0000 size=0282ch ( 10284) load
I (102) esp_image: segment 2: paddr=00019608 vaddr=40080000 size=06a10h ( 27152) load
I (114) esp_image: segment 3: paddr=00020020 vaddr=400d0020 size=0b0d8h ( 45272) map
I (130) esp_image: segment 4: paddr=0002b100 vaddr=40086a10 size=03a30h ( 14896) load
I (136) esp_image: segment 5: paddr=0002eb38 vaddr=50000000 size=00028h (    40) load
I (142) boot: Loaded app from partition at offset 0x10000
I (142) boot: Disabling RNG early entropy source...
I (156) cpu_start: Multicore app
I (164) cpu_start: GPIO 3 and 1 are used as console UART I/O pins
I (164) cpu_start: Pro cpu start user code
I (164) cpu_start: cpu freq: 160000000 Hz
I (166) app_init: Application information:
I (170) app_init: Project name:     hello_world
I (174) app_init: App version:      1
I (178) app_init: Compile time:     May  7 2026 18:26:20
I (183) app_init: ELF file SHA256:  bfa35979b...
I (187) app_init: ESP-IDF:          v6.1-dev-4506-g88add2513f
I (192) efuse_init: Min chip rev:     v0.0
I (196) efuse_init: Max chip rev:     v3.99
I (200) efuse_init: Chip rev:         v3.1
I (204) heap_init: Initializing. RAM available for dynamic allocation:
I (210) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (215) heap_init: At 3FFB3168 len 0002CE98 (179 KiB): DRAM
I (221) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (226) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (232) heap_init: At 4008A440 len 00015BC0 (86 KiB): IRAM
I (238) spi_flash: detected chip: generic
I (240) spi_flash: flash io: dio
W (243) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (257) main_task: Started on CPU0
I (267) main_task: Calling app_main()
Hello world!
This is esp32 chip with 2 CPU core(s), WiFi/BTBLE, silicon revision v3.1, 2MB external flash
Minimum free heap size: 304620 bytes
Restarting in 10 seconds...
Restarting in 9 seconds...
Restarting in 8 seconds...
Restarting in 7 seconds...
Restarting in 6 seconds...
Restarting in 5 seconds...
Restarting in 4 seconds...
Restarting in 3 seconds...
Restarting in 2 seconds...
Restarting in 1 seconds...
Restarting in 0 seconds...
Restarting now.
ets Jul 29 2019 12:21:46
(繰り返し)
```

---

以下オリジナルのまま

---

| Supported Targets | ESP32 | ESP32-C2 | ESP32-C3 | ESP32-C5 | ESP32-C6 | ESP32-C61 | ESP32-H2 | ESP32-H21 | ESP32-H4 | ESP32-P4 | ESP32-S2 | ESP32-S3 | ESP32-S31 | Linux |
| ----------------- | ----- | -------- | -------- | -------- | -------- | --------- | -------- | --------- | -------- | -------- | -------- | -------- | --------- | ----- |

# Hello World Example

Starts a FreeRTOS task to print "Hello World".

(See the README.md file in the upper level 'examples' directory for more information about examples.)

## How to use example

Follow detailed instructions provided specifically for this example.

Select the instructions depending on Espressif chip installed on your development board:

- [ESP32 Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/stable/get-started/index.html)
- [ESP32-S2 Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/get-started/index.html)

## Example folder contents

The project **hello_world** contains one source file in C language [hello_world_main.c](main/hello_world_main.c). The file is located in folder [main](main).

ESP-IDF projects are built using CMake. The project build configuration is contained in `CMakeLists.txt` files that provide set of directives and instructions describing the project's source files and targets (executable, library, or both).

Below is short explanation of remaining files in the project folder.

```
├── CMakeLists.txt
├── pytest_hello_world.py      Python script used for automated testing
├── main
│   ├── CMakeLists.txt
│   └── hello_world_main.c
└── README.md                  This is the file you are currently reading
```

For more information on structure and contents of ESP-IDF projects, please refer to Section [Build System](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html) of the ESP-IDF Programming Guide.

## Troubleshooting

- Program upload failure
  - Hardware connection is not correct: run `idf.py -p PORT monitor`, and reboot your board to see if there are any output logs.
  - The baud rate for downloading is too high: lower your baud rate in the `menuconfig` menu, and try again.

## Technical support and feedback

Please use the following feedback channels:

- For technical queries, go to the [esp32.com](https://esp32.com/) forum
- For a feature request or bug report, create a [GitHub issue](https://github.com/espressif/esp-idf/issues)

We will get back to you as soon as possible.
