*****************
Build the Backend
*****************

    SimCenterBackendApplications contains many applications written in C++, C, and Python that are needed by all SimCenter User Interfaces. To build the backend, you will need to follow these steps:

    1. Clone the `SimCenterBackendApplications repository <https://github.com/NHERI-SimCenter/SimCenterBackendApplications>`_. 
    2. Build SimCenterBackendApplications using the following steps:

        2.1. Create a build directory for the build output. This can be done in the terminal using the command ``mkdir build``.

        2.2. Install the backend dependencies using Conan. You can do this by going to the newly created build directory and running the command:

            ``conan install .. --build missing``

            This will install all the dependencies and will build dependencies from their source code as needed.
        
        2.3. Run CMake configuration. This can be done using the command ``cmake ..``. Depending on your build environment, especially if you have multiple compilers, you may need to select a specific CMake generator. For instance, on Windows using Visual Studio 2017, you can configure CMake as follows:

            ``cmake .. -G "Visual Studio 15 2017 Win64"``

        2.4. Build the release version of the backend. This can be done using the generated build system. For instance, on Unix-based systems when using make files, this can be achieved using the command ``make`` or ``make release``. When using an IDE like Visual Studio on Windows or XCode on Mac, the generated project can be opened in the IDE and used to build the code. Additionally, this can also be done from the terminal using the CMake command:

            ``cmake --build . --config Release``

    3. Install the backend applications to a local folder. This can be done by building the ``install target`` when using make on Unix-based systems. This can also be done from an IDE (e.g., by selecting the install target or project and building it). Additionally, this can be done from the terminal using the command:
        
        ``cmake --build . --target install`` or ``cmake --install`` if you have CMake 3.15 or later. If the build and installation were successful, you should find a folder called ``applications`` in the repository with all the applications inside it.
