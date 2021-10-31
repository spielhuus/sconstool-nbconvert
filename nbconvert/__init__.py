#
# Copyright (c) 2013 Henry Gomersall <heng@kedevelopments.co.uk>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import SCons.Builder
import SCons.Tool
from SCons.Errors import StopError

import os

def render_nbconvert_template(target, source, env):

    jupyter = 'jupyter nbconvert --output=%s' % target[0].path
    for c in env.Dictionary().get('NBCONVERT_ENVIRONMENT_VARS') :
        if c == 'to' :            
            jupyter += ' --to %s' % (env.Dictionary().get('NBCONVERT_ENVIRONMENT_VARS').get(c))
        elif c == 'no-input' :
            jupyter += ' --no-input'
        else :
            jupyter += ' --%s=%s' % (c, env.Dictionary().get('NBCONVERT_ENVIRONMENT_VARS').get(c))
    jupyter += ' %s' % source[0].path
    env.Execute(jupyter)

    return None

def generate(env):

    print("generate nbconvert")
    env.SetDefault(NBCONVERT_ENVIRONMENT_VARS={})
    env['BUILDERS']['nbconvert'] = SCons.Builder.Builder(
            action=render_nbconvert_template)

def exists(env):
    print("test library")
    # try:
    #     import nbconvert
    # except ImportError as e:
    #     raise StopError(ImportError, e.message) 
