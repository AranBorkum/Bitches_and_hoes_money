# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.12.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.12.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/aranborkum/General/MCMoney-Maker/MCCPP/source

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/aranborkum/General/MCMoney-Maker/MCCPP/build

# Include any dependencies generated for this target.
include CMakeFiles/MakeMoney.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/MakeMoney.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MakeMoney.dir/flags.make

CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o: CMakeFiles/MakeMoney.dir/flags.make
CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o: /Users/aranborkum/General/MCMoney-Maker/MCCPP/source/MakeMoney.cxx
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/aranborkum/General/MCMoney-Maker/MCCPP/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o -c /Users/aranborkum/General/MCMoney-Maker/MCCPP/source/MakeMoney.cxx

CMakeFiles/MakeMoney.dir/MakeMoney.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MakeMoney.dir/MakeMoney.cxx.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/aranborkum/General/MCMoney-Maker/MCCPP/source/MakeMoney.cxx > CMakeFiles/MakeMoney.dir/MakeMoney.cxx.i

CMakeFiles/MakeMoney.dir/MakeMoney.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MakeMoney.dir/MakeMoney.cxx.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/aranborkum/General/MCMoney-Maker/MCCPP/source/MakeMoney.cxx -o CMakeFiles/MakeMoney.dir/MakeMoney.cxx.s

# Object files for target MakeMoney
MakeMoney_OBJECTS = \
"CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o"

# External object files for target MakeMoney
MakeMoney_EXTERNAL_OBJECTS =

MakeMoney: CMakeFiles/MakeMoney.dir/MakeMoney.cxx.o
MakeMoney: CMakeFiles/MakeMoney.dir/build.make
MakeMoney: CMakeFiles/MakeMoney.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/aranborkum/General/MCMoney-Maker/MCCPP/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable MakeMoney"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MakeMoney.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MakeMoney.dir/build: MakeMoney

.PHONY : CMakeFiles/MakeMoney.dir/build

CMakeFiles/MakeMoney.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MakeMoney.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MakeMoney.dir/clean

CMakeFiles/MakeMoney.dir/depend:
	cd /Users/aranborkum/General/MCMoney-Maker/MCCPP/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/aranborkum/General/MCMoney-Maker/MCCPP/source /Users/aranborkum/General/MCMoney-Maker/MCCPP/source /Users/aranborkum/General/MCMoney-Maker/MCCPP/build /Users/aranborkum/General/MCMoney-Maker/MCCPP/build /Users/aranborkum/General/MCMoney-Maker/MCCPP/build/CMakeFiles/MakeMoney.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/MakeMoney.dir/depend
