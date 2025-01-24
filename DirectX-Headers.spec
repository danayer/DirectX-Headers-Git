Name:           DirectX-Headers
Version:        1.610.0
Release:        1%{?dist}
Summary:        DirectX headers for using D3D12

%global commit 34c98665f205e5a9457cd6487ba0b5a10e8b634f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
%global giturl  %{url}
Source0:        %{giturl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  git

%description
DirectX headers for using D3D12

%prep
%setup -q -n DirectX-Headers-%{commit}

%build
%meson \
    -Dbuild-test=false
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_includedir}/directx/
%{_includedir}/wsl/
%{_libdir}/cmake/DirectX-Headers/
%{_libdir}/pkgconfig/DirectX-Headers.pc

%changelog
* %(date '+%a %b %d %Y') %{packager} - 1.610.0-1
- Initial package
