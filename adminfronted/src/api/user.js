import request from '@/utils/request'
import {apiuri} from '@/config'

// users
export function postUser(data) {
  return request({
    url: apiuri.users,
    method: 'post',
    data
  })
}

export function getUser(query) {
  return request({
    url: apiuri.users,
    method: 'get',
    params: query
  })
}

export function patchUser(id, data) {
  return request({
    url: apiuri.users + id + '/',
    method: 'patch',
    data
  })
}

export function deleteUser(id) {
  return request({
    url: apiuri.users + id + '/',
    method: 'delete'
  })
}

// groups
export function postGroup(data) {
  return request({
    url: apiuri.groups,
    method: 'post',
    data
  })
}

export function getGroup(query) {
  return request({
    url: apiuri.groups,
    method: 'get',
    params: query
  })
}

export function putGroup(id, data) {
  return request({
    url: apiuri.groups + id + '/',
    method: 'put',
    data
  })
}

export function deleteGroup(id) {
  return request({
    url: apiuri.groups + id + '/',
    method: 'delete'
  })
}

// roles
export function postRole(data) {
  return request({
    url: apiuri.roles,
    method: 'post',
    data
  })
}

export function getRole(query) {
  return request({
    url: apiuri.roles,
    method: 'get',
    params: query
  })
}

export function putRole(id, data) {
  return request({
    url: apiuri.roles + id + '/',
    method: 'put',
    data
  })
}

export function deleteRole(id) {
  return request({
    url: apiuri.roles + id + '/',
    method: 'delete'
  })
}
