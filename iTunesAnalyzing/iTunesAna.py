# This module provides an interface for reading and writing the “property list” XML files used mainly by Mac OS X.
import plistlib


def findDuplicates(fileName):
    print('Finding duplicate tracks in %s ...' % fileName)
    # read in a playlist
    plist = plistlib.load(fileName)
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']  # Tracks 字典
    # create a track name dictionary
    tracksNames = {}
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # look for existing entries
            if name in tracksNames:
                # if a name and duration match, increment the count
                # round the track length to the nearest second
                if duration // 1000 == tracksNames[name][0] // 1000: # // 取整除 - 返回商的整数部分（向下取整）
                    count = tracksNames[name][1]
                    tracksNames[name] = (duration, count + 1)
                else:
                    # add dictionary entry as tuple (duration, count)
                    tracksNames[name] = (duration, 1)
        except:
            # ignore
            pass
     # store duplicates as (name, count) tuples
    dups = []
    for k, v in tracksNames.items():
         if v[1] > 1:
             dups.append(v[1], k)
    # save duplicates to a file
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
    else:
        print("No duplicate tracks found!")
    f = open("dups.txt", "w")
    for val in dups:
        f.write("[%d] $s \n" % (val[0], val[1]))
    f.close()


findDuplicates("rating.xml")


