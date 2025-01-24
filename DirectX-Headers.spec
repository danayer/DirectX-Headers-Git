Name:           DirectX-Headers
Version:        1.610.0.1
Release:        1%{?dist}
Summary:        DirectX headers for using D3D12
# LastCommit:   358fbfca04e8c65784397d8184f161d64bfe569e

License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
Source0:        %{url}/archive/%{commit}/DirectX-Headers-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build

%description
DirectX headers for using D3D12

%prep
%autosetup -n %{name}-main

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
