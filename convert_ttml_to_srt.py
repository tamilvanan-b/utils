import sys
import pysubs2

def convert_ttml_to_srt(ttml_filepath, srt_filepath):
    try:
        subs = pysubs2.load(ttml_filepath)
        subs.save(srt_filepath)
        print(f"Successfully converted '{ttml_filepath}' to '{srt_filepath}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    srt_file = "output.srt"
    convert_ttml_to_srt(sys.argv[1], srt_file)