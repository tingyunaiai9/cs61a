from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

octave = 1 # 音高

c_freq = 261.63
d_freq = 293.66
e_freq = 329.63
f_freq = 349.23
rise_f_freq = 369.99
g_freq = 392.00
a_freq = 440.00
b_freq = 493.88


def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.htmlg)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    """Write the output of the sampler function as a wav file.
    See https://docs.python.org/3/library/wave.html
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < frame_rate * seconds:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

c = tri(octave * c_freq)
d = tri(octave * d_freq)
e = tri(octave * e_freq)
f = tri(octave * f_freq)
rise_f = tri(octave * rise_f_freq)
g = tri(octave * g_freq)
a = tri(octave * a_freq)
b = tri(octave * b_freq)

low_e = tri(octave * e_freq / 2)
low_f = tri(octave * f_freq / 2)
low_rise_f = tri(octave * rise_f_freq / 2)
low_g = tri(octave * g_freq / 2)
low_a = tri(octave * a_freq / 2)
low_b = tri(octave * b_freq / 2)


def castle_in_the_sky():

    beat = 2/3  # 一拍为2/3秒

    z = 0.0

    # 1
    song = note(low_a, z, z+1/2*beat)
    z += 1/2*beat
    song = both(song, note(low_b, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(c, z, z+3/2*beat))
    z += 3/2*beat
    song = both(song, note(low_b, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(c, z, z+1*beat))
    z += 1*beat
    song = both(song, note(e, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_b, z, z+3*beat))
    z += 3*beat

    # 2
    song = both(song, note(low_e, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_a, z, z+3/2*beat))
    z += 3/2*beat
    song = both(song, note(low_g, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(low_a, z, z+1*beat))
    z += 1*beat
    song = both(song, note(c, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_g, z, z+3*beat))
    z += 3*beat

    # 3
    song = both(song, note(low_e, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_f, z, z+3/2*beat))
    z += 3/2*beat
    song = both(song, note(low_e, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(low_f, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(c, z, z+3/2*beat))
    z += 3/2*beat
    song = both(song, note(low_e, z, z+3*beat))
    z += 3*beat

    # 4
    song = both(song, note(c, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_b, z, z+3/2*beat))
    z += 3/2*beat
    song = both(song, note(low_rise_f, z, z+1/2*beat))
    z += 1/2*beat
    song = both(song, note(low_rise_f, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_b, z, z+1*beat))
    z += 1*beat
    song = both(song, note(low_b, z, z+3*beat))
    z += 3*beat

    # # 5
    # song = note(low_a, z, z+1/2*beat)
    # z += 1/2*beat
    # song = both(song, note(low_b, z, z+1/2*beat))
    # z += 1/2*beat
    # song = both(song, note(c, z, z+3/2*beat))
    # z += 3/2*beat
    # song = both(song, note(low_b, z, z+1/2*beat))
    # z += 1/2*beat
    # song = both(song, note(c, z, z+1*beat))
    # z += 1*beat
    # song = both(song, note(e, z, z+1*beat))
    # z += 1*beat
    # song = both(song, note(low_b, z, z+3*beat))
    # z += 3*beat

    # # 6
    # song = both(song, note(low_e, z, z+1/2*beat))
    # z += 1/2*beat
    # song = both(song, note(low_e, z, z+1/2*beat))
    # z += 1/2*beat
    # song = both(song, note(low_a, z, z+3/2*beat))
    # z += 3/2*beat
    # song = both(song, note(low_g, z, z+1/2*beat))
    # z += 1/2*beat
    # song = both(song, note(low_a, z, z+1*beat))
    # z += 1*beat
    # song = both(song, note(c, z, z+1*beat))
    # z += 1*beat
    # song = both(song, note(low_g, z, z+3*beat))
    # z += 3*beat

    return song, z

song, seconds = castle_in_the_sky()
play(song, 'castle_in_the_sky.wav', seconds)
