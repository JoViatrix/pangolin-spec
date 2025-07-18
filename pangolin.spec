%global commit 4235555
%global datetimever 202507181445%{commit}

Name: pangolin
Version: %{datetimever}
Release: %autorelease.1
Summary: Lightweight and portable utility libraries for prototyping 3D, numeric or video based programs and algorithms.

License: MIT
URL: https://github.com/stevenlovegrove/Pangolin


Provides: libpango_python.so()(64bit)


BuildRequires: wayland-devel
BuildRequires: libxkbcommon-devel
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libepoxy-devel
BuildRequires: eigen3
BuildRequires: cmake
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: openexr-devel
BuildRequires: catch2-devel
BuildRequires: libdc1394-devel
BuildRequires: libraw1394-devel
BuildRequires: librealsense-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: git

%ifarch x86_64
BuildRequires: openni-devel
%endif


%description
Pangolin is a set of lightweight and portable utility libraries for prototyping 3D, numeric or video based programs and algorithms. It is used quite widely in the field of Computer Vision as a means to remove platform-specific boilerplate and make it easy to visualize data.

The general ethos of Pangolin is to minimize boilerplate and maximize portability and flexibility through simple interfaces and factories over things like windowing and video. It also offers a suite of utilities for interactive debugging, such as 3D manipulation, plotters, tweak variables, and a drop-down Quake-like console for python scripting and live tweaking.

%prep
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git %{name}-%{commit}
cd %{name}-%{commit}
git checkout %{commit}
git submodule update --init --recursive


%build
%cmake -GNinja %{name}-%{commit}
%cmake_build


%install
%cmake_install


%check


%files
%license
%doc

%{_bindir}/Plotter
%{_bindir}/VideoConvert
%{_bindir}/VideoJsonPrint
%{_bindir}/VideoJsonTransform
%{_bindir}/VideoViewer

%{_includedir}/NaturalSort/*
%{_includedir}/dynalo/*
%{_includedir}/pangolin/*
%{_includedir}/sigslot/*
%{_includedir}/tinyobj/tiny_obj_loader.h

%{_libdir}/cmake/Pangolin/*
%{_libdir}/libpango*
%{_libdir}/libtinyobj*

%changelog
%autochangelog

