%global debug_package %{nil}
%global __strip /bin/true

# There is no LTO in mesa, so drop that in stub archives also
# see mesa comment:
# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now
%define _lto_cflags %{nil}

Name:           DirectX-Headers
Version:        1.615.1.49
Release:        1%{?dist}
Summary:        Official Direct3D 12 headers

%global commit 33374754f65baac0500dda6187e371136357246f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
%global giturl  %{url}
Source0:        %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# WSL2 is only relevant on theses arches so far
ExclusiveArch:  x86_64 aarch64 %{ix86}

BuildRequires:  meson
BuildRequires:  gcc-c++
# Test assumes the build is under WSL, which is unlikely
%{?_with_test:BuildRequires: gtest-devel}

# Case in-sensitive provides
Provides: directx-headers = %{version}-%{release}


%description
Official Direct3D 12 headers

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# This only provides -static files, so only
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}
for i in LICENSE README.md ; do
  sed -i -e 's/\r$//' ${i}
  touch -r SECURITY.md ${i}
done


%build
%meson \
 %{?!_with_test:-Dbuild-test=false}

%meson_build


%install
%meson_install


%check
%{?_with_test:
%meson_test
}

%files
%license LICENSE
%doc README.md SECURITY.md
%{_includedir}/directx
%{_includedir}/dxguids
%{_includedir}/wsl
%{_libdir}/pkgconfig/DirectX-Headers.pc
%{_libdir}/libDirectX-Guids.a
%{_libdir}/libd3dx12-format-properties.a

%files devel
%license LICENSE
%doc README.md SECURITY.md
%{_includedir}/directx
%{_includedir}/dxguids
%{_includedir}/wsl
%{_libdir}/libDirectX-Guids.a
%{_libdir}/libd3dx12-format-properties.a
%{_libdir}/pkgconfig/DirectX-Headers.pc


%changelog
* Thu Nov 28 2024 Nicolas Chauvet <kwizart@gmail.com> - 1.614.1-1
- Update to 1.614.1

* Fri Apr 12 2024 Nicolas Chauvet <kwizart@gmail.com> - 1.613.1-1
- Update to 1.613.1

* Mon Feb 26 2024 Nicolas Chauvet <kwizart@gmail.com> - 1.611.0-1
- Initial spec file
