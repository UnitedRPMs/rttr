# 
%define _legacy_common_support 1

Name:           rttr
Version:        0.9.6
Release:        1%{?dist}
Summary:        Run Time Type Reflection for C++
License:        MIT
Group:          Development/Libraries
URL:            https://www.rttr.org/
Source0:        https://www.rttr.org/releases/rttr-%{version}-src.tar.gz

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package -n librttr
Summary:        Run Time Type Reflection for C++
Group:          Development/Libraries

%description -n librttr
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package  -n librttr-devel
Summary:        Header files for the C++ Run Time Type Reflection library
Group:          Development/Libraries
Requires:       librttr = %{version}

%description  -n librttr-devel
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.


%prep
%autosetup -n %{name}-%{version} 
# Fix incorrect file permissions after install
sed -i 's/PERMISSIONS OWNER_READ//' CMake/*.cmake

%build
find . -type f -exec chmod a-x "{}" +
dos2unix README.md

%cmake3 -DBUILD_BENCHMARKS=OFF \
    -DCMAKE_INSTALL_CMAKEDIR=cmake \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_UNIT_TESTS=OFF \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DBUILD_PACKAGE=OFF .

%cmake_build

%install
%cmake_install 

# Move doc into system dir
mv -f %{buildroot}/usr/doc %{buildroot}/%{_datadir}/

%post -n librttr -p /sbin/ldconfig
%postun -n librttr -p /sbin/ldconfig

%files -n librttr
%license LICENSE.txt
%{_libdir}/librttr_core.so.%{version}
%{_datadir}/rttr/*.txt
%{_datadir}/rttr/*.md
%{_docdir}/index.html
%{_docdir}/rttr-0-9-6/

%files -n librttr-devel
%{_includedir}/rttr/
%{_libdir}/librttr_core.so
%{_datadir}/rttr/cmake/


%changelog
* Mon May 18 2020 David Va <davidva AT tuta DOT io> - 0.9.6-1
- Initial build
