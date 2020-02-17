from . import _clib

def png_optimize(
        png_bytes: bytes,
        verbose=False,
        lossy_transparent=False,
        lossy_8bit=False,
        filter_strategies:str =None,
        keepchunks: list = None,
        use_zopfli=True,
        num_iterations=15,
        num_iterations_large=20):
    '''
    Compress the image by calling this method
        usage：
            ---------------------------------------
            # a simple example, using the default configuration
            data = open('test.png', 'rb').read()
            result, code = png_optimize(data)
            # if code ==0 ,png compression success
            if code == 0:
                # save png
                with open('result.png','wb') as f:
                    f.write(result)
                    f.close()
            ---------------------------------------
            # use quick, but not very good, compression
            png_optimize(data, use_zopfli=False)

            # Compress really good and trying all filter strategies
            png_optimize(data, lossy_8bit=True, lossy_transparent=True, filter_strategies='01234mepb', num_iterations=500)

        If you want to process multiple images, use multiprocessing
            
    :param png_bytes: PNG bytes
    :param verbose: print message
    :param lossy_transparent: remove colors behind alpha channel 0.No visual difference, removes hidden information.
    :param lossy_8bit: convert 16-bit per channel image to 8-bit per channel.
    :param filter_strategies: filter strategies to try:
        0-4: give all scanlines PNG filter type 0-4
        m: minimum sum
        e: entropy
        p: predefined (keep from input, this likely overlaps another strategy
        b: brute force (experimental)
        By default, if this argument is not given, 
        one that is most likely the best for this image is 
        chosen by trying faster compression with each type.

    :param keepchunks: keep metadata chunks with these names that would normally be removed.
        example:  keepchunks=['tEXt','zTXt','iTXt','gAMA']
    :param use_zopfli: if not, use quick, but not very good, compression
    :param num_iterations: num iterations
    :param num_iterations_large: max num iterations
    :return: PNG optimize bytes results and code ,if code ==0, png compression success
    '''
    return _clib.zopfli_png_optimize(
        png_bytes,
        verbose,
        lossy_transparent,
        lossy_8bit,
        filter_strategies,
        keepchunks,
        use_zopfli,
        num_iterations,
        num_iterations_large if num_iterations<num_iterations_large else num_iterations
    )
