# Archive.org scraper

I made this program to make it easier to only grab the ROM links I want from ROM megathread links (more specifically, only USA roms). 

I personally use JDownloader 2 as my download manager and highly recommend that you do as well if you plan on downloading ROMs from archive.org. It speeds up downloads and works in conjunction with this program.

If you are downloading Jdownloader 2 for the first time, please make sure you enable the archive.org plugin. 

I also recommend turning off extracting after downloading if you are downloading a lot of files. This will needlessly increase the amount of space you will need to download all the files.

Also, change your max chunks per download/max simultaneous downloads to 3-5. Play around with this and see what works best. It will increase your download speeds if set up properly.

# Table of contents

- [Archive.org scraper](#archiveorg-scraper)
- [Prerequisites](#prerequisites)
- [How to use](#how-to-use)

# Prerequisites

### Getting the Webdriver
First, you will need to download the webdriver for your browser of choice. 

Supported browsers are Chrome, Firefox, or Opera. 
Before you download, be sure to get the 32-bit version if your computer is 32-bit, or the 64-bit version if your computer is 64-bit.
If using Chrome, there will only be a 32-bit version. However, it is compatible with both 32 and 64-bit systems.

Webdriver links:
[Chrome](http://chromedriver.chromium.org/downloads)
[Firefox](https://github.com/mozilla/geckodriver/releases)
[Opera](https://github.com/operasoftware/operachromiumdriver/releases)


After downloading your preferred webdriver, create a folder anywhere (except your Program Files(x86) folder!) and name it whatever you want. 

I personally put mine in my 'C:\Program Files' folder and named ChromeDriver. 

However, do NOT put this in your Program Files(x86) folder, it may not work properly. 

Once you have done that, extract the webdriver from the archive to the directory you just created. 

![1](https://i.imgur.com/Dsvcjau.png)

Now, copy the link of the webdriver's directory, you will have to add this your your system PATH variables.

![2](https://i.imgur.com/lW7wm19.png)

### Adding webdriver to PATH

To add this your your system PATH, type "path" into windows search and hit enter.

![3](https://i.imgur.com/NRuH3jJ.png)

You can also find this by navigating to Control Panel>System>Advanced System Settings.

Now, click on the "Environment Variables..." button

![4](https://i.imgur.com/xLzNksX.png)

### IMPORTANT!!!

Please be careful during this part, editing your path variables can be very dangerous if you don't know what you're doing.

First, you may have a Path variable under your user variables. Ignore this, you want to change your system path variables. 

Second, when adding a path variable, click on Path, then click edit. DO NOT delete and replace everything in your path. I have made this mistake before and trust me, you do not want to make the same mistake. 

If you are confused about anything I just said, just do exactly as I do in the pictures and I promise you will be okay.

![5](https://i.imgur.com/N2N6rj2.png)

After you click edit, you will be shown a list of all of your path variables. 

Click new on the top right. This will create an empty entry. Copy and paste the directory of the webdriver that you copied earlier into this entry, then click Ok, and then ok again to close the windows and save the changes.

![6](https://i.imgur.com/jcZ6KXc.png)

Once this is complete, you should now be able to run the program! 


# How to use

When you first run the program, you will be prompted to select your web browser. Just type in whatever you're using and hit enter.

![7](https://i.imgur.com/MbJsTOH.png)

The browser you entered should now open with an empty page.

Next, you will be prompted to enter the repository's URL. For legal reasons, I will not provide the links, just Google roms megathread.

The page you're looking for should look something like this, containing a bunch of file names and links:

![8](https://i.imgur.com/tASdMaI.png)

Now, the program will ask you what text to look for and keep the link if it contains it.

In my case, I will type in '(USA' (no quotes). The reason I don't use '(USA)' is because some ROMs will have the region (USA, Europe) and therefore the program will not find (USA) in (USA, Europe). Keep this in mind, as you may accidentally skip a ROM you wanted if you're not careful.

After this, it will ask if you wish to grab extras. Just type 'y' if you want to include betas/prototypes/demos or 'n' to ignore them. 

Note that this works by simply checking if (Beta, (Demo, or (Proto are in the title. 

If the repository you choose uses a different naming convention, this will not work and simply just end up grabbing all the links.

![9](https://i.imgur.com/wlVG1xo.png)

The program should now start grabbing the links and writing them a file named links.txt which can be found in the program's directory.

Now, open Jdownloader 2, then open the links.txt file with all the links that you grabbed.

In the links.txt file, press ctrl-A followed by ctrl-C to highlight all and copy the links.

Jdownloader 2 should have automatically detected all the links and added them. If it doesnt, you can manually add them like this:

![10](https://i.imgur.com/6MoYpkP.png)

You should now have a bunch of links ready to download. Right click one of them and click "start all downloads"!

![11](https://i.imgur.com/ak43Spa.png)









