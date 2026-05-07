# esp-idf-hello-world

[esp\-idf/examples/get\-started/hello\_world at master · espressif/esp\-idf · GitHub](https://github.com/espressif/esp-idf/tree/master/examples/get-started/hello_world)
をやってみた。

環境は

- ESP32-WROVER のカメラ付きのやつ([FNK0060](https://www.amazon.co.jp/dp/B0CJJHXD1W))
- Windows11 の WSL2(Ubuntu)上で開発
- IDF は 6.1
- EIM なしでやってみた。やっぱいろいろ辛いので、EIM で試す

手順はこんな感じ

0. Windows 側で usbipd.exe(`winget install dorssel.usbipd-win`) と [CH340 ドライバ](https://www.wch-ic.com/search?q=CH340&t=downloads)(ESP32-WROVER だから)
1. [USB デバイスを接続する](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb#attach-a-usb-device) で WSL に接続
1. [ステップ1\. 前提条件のインストール](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-1-install-prerequisites)
1. [ステップ2\. ESP\-IDFを取得する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-2-get-esp-idf) - でかい。2.4G あった
3. [ステップ3．ツールをセットアップする](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup-legacy.html#step-3-set-up-the-tools) - とりあえず毎回 `. $HOME/esp/esp-idf/export.sh` を実行することにする
4. [プロジェクトを開始する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#start-a-project) - パスは`~/esp/hello_world` でなくてもどこでも OK
5. [プロジェクトの設定](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#configure-your-project) - TUI のメニューは何もしないで `Q`
6. [プロジェクトを構築する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#build-the-project)
7. [デバイスにフラッシュする](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#flash-onto-the-device) - ここで PORT に `/dev/ttyUSB0`
8. [出力を監視する](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-start-project.html#monitor-the-output)  - ここでも PORT に `/dev/ttyUSB0`


毎回

```sh
. $HOME/esp/esp-idf/export.sh
code .
```
は面倒。あと IDF の VScode 拡張がいろいろうるさいのもやだ。EIM にするといいらしいのであとで試す。

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
