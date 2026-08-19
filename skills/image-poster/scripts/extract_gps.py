#!/usr/bin/env python3
"""
Extract GPS coordinates and location information from image EXIF metadata.
Returns JSON with latitude, longitude, formatted coordinates string, or null if no GPS data.
"""

import sys
import json
import subprocess
from pathlib import Path

def get_gps_from_exif(image_path):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS, GPSTAGS
        
        img = Image.open(image_path)
        exif = img._getexif()
        if not exif:
            return None
        
        gps_info = {}
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                for t in value:
                    sub_tag = GPSTAGS.get(t, t)
                    gps_info[sub_tag] = value[t]
        
        if not gps_info:
            return None
        
        def dms_to_deg(dms, ref):
            deg = float(dms[0])
            minute = float(dms[1])
            sec = float(dms[2])
            val = deg + (minute / 60.0) + (sec / 3600.0)
            if ref in ['S', 'W']:
                val = -val
            return val

        lat_raw = gps_info.get('GPSLatitude')
        lat_ref = gps_info.get('GPSLatitudeRef', 'N')
        lon_raw = gps_info.get('GPSLongitude')
        lon_ref = gps_info.get('GPSLongitudeRef', 'E')
        
        if lat_raw and lon_raw:
            lat = dms_to_deg(lat_raw, lat_ref)
            lon = dms_to_deg(lon_raw, lon_ref)
            
            lat_str = f"{abs(lat):.4f}° {'N' if lat >= 0 else 'S'}"
            lon_str = f"{abs(lon):.4f}° {'E' if lon >= 0 else 'W'}"
            
            return {
                "has_gps": True,
                "latitude": lat,
                "longitude": lon,
                "coordinates": f"{lat_str}, {lon_str}"
            }
    except Exception:
        pass
    
    # Fallback to macOS mdls
    try:
        res = subprocess.run(
            ["mdls", "-name", "kMDItemLatitude", "-name", "kMDItemLongitude", str(image_path)],
            capture_output=True,
            text=True
        )
        out = res.stdout
        lat = None
        lon = None
        for line in out.splitlines():
            if "kMDItemLatitude" in line and "(null)" not in line:
                lat = float(line.split("=")[-1].strip())
            elif "kMDItemLongitude" in line and "(null)" not in line:
                lon = float(line.split("=")[-1].strip())
        if lat is not None and lon is not None:
            lat_str = f"{abs(lat):.4f}° {'N' if lat >= 0 else 'S'}"
            lon_str = f"{abs(lon):.4f}° {'E' if lon >= 0 else 'W'}"
            return {
                "has_gps": True,
                "latitude": lat,
                "longitude": lon,
                "coordinates": f"{lat_str}, {lon_str}"
            }
    except Exception:
        pass
    
    return {"has_gps": False, "coordinates": None}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing image path argument"}))
        sys.exit(1)
    
    path = sys.argv[1]
    result = get_gps_from_exif(path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
